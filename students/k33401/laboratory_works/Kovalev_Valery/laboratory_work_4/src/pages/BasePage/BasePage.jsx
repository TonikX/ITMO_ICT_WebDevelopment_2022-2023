import { Layout, Menu } from "antd";
import React, { useMemo, useState } from "react";
import { FormOutlined, HomeOutlined, LoginOutlined, SearchOutlined, UserOutlined } from "@ant-design/icons";
import LoginModal from "../../modals/LoginModal";
import RegisterModal from "../../modals/RegisterModal";
import { useAuth } from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import CollectionModal from "../../modals/CollectionModal";
import {useProfile} from "../../hooks/useProfile";

function getItem(label, key, icon, children) {
    return {
        key,
        icon,
        children,
        label,
    };
}

const NavigateItems = [getItem("Main", "main", <HomeOutlined />), getItem("Search", "search", <SearchOutlined />)];

const LoggedNavigateItems = [
    getItem("Profile", "profile", <UserOutlined />),
    getItem("Main", "main", <HomeOutlined />),
    getItem("Search", "search", <SearchOutlined />),
];

const AuthItems = [getItem("Log In", "login", <LoginOutlined />), getItem("Register", "register", <FormOutlined />)];

const BasePage = ({ pageName, children, ref }) => {
    const { Sider, Content } = Layout;
    const [collapsed, setCollapsed] = useState(false);
    const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
    const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);
    const { searchWord, tone } = useSelector((state) => state.search);
    const navigate = useNavigate();

    const searchLink = useMemo(() => {
        if (searchWord && tone) {
            return `/search/${searchWord}/${tone}`;
        } else if (searchWord && !tone) {
            return `/search/${searchWord}`;
        } else {
            return "/search";
        }
    }, [searchWord, tone]);

    const menuOnClick = (e) => {
        switch (e.key) {
            case "login":
                setIsLoginModalOpen(true);
                break;
            case "register":
                setIsRegisterModalOpen(true);
                break;
            case "main":
                navigate("/");
                break;
            case "search":
                navigate(searchLink);
                break;
            case "profile":
                navigate("/profile");
                break;
            default:
                break;
        }
    };

    const { isAuth } = useAuth();
    useProfile()


    return (
        <Layout className="min-h-screen" ref={ref}>
            <LoginModal isLoginModalOpen={isLoginModalOpen} setIsLoginModalOpen={setIsLoginModalOpen} />
            <RegisterModal isRegisterModalOpen={isRegisterModalOpen} setIsRegisterModalOpen={setIsRegisterModalOpen} />
            <CollectionModal/>

            <Sider
                collapsible
                style={{ position: "sticky", overflow: "auto", height: "100vh", left: 0, top: 0 }}
                collapsed={collapsed}
                onCollapse={(value) => setCollapsed(value)}
            >
                {isAuth ? (
                    <>
                        <Menu
                            theme="dark"
                            onClick={menuOnClick}
                            selectedKeys={[pageName]}
                            mode="inline"
                            items={LoggedNavigateItems}
                        />
                    </>
                ) : (
                    <>
                        <Menu selectable={false} onClick={menuOnClick} theme="dark" mode="inline" items={AuthItems} />
                        <Menu
                            theme="dark"
                            onClick={menuOnClick}
                            selectedKeys={[pageName]}
                            mode="inline"
                            items={NavigateItems}
                        />
                    </>
                )}
            </Sider>
            <Layout className="site-layout p-2">
                <Content>{children}</Content>
            </Layout>
        </Layout>
    );
};

export default BasePage;
