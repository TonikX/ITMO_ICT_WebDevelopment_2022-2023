import React, {useEffect, useState} from "react";
import BasePage from "./BasePage/BasePage";
import {useDispatch, useSelector} from "react-redux";
import {fetchCollections, fetchLikes} from "../store/actions/profileActions";
import Album from "../components/Album";
import {useAuth} from "../hooks/useAuth";
import ChoiceLikesCollections from "../components/profilePage/Choice/ChoiceLikesCollections";
import CollectionAlbum from "../components/profilePage/Collections/CollectionAlbum";
import {Button} from "antd";
import {LogoutOutlined} from "@ant-design/icons";
import {logOut} from "../store/actions/authActions";
import {useNavigate} from "react-router-dom";


const ProfilePage = () => {
    const dispatch = useDispatch();
    const {likedPhotos, collections} = useSelector(state=>state.profile)
    const {user} = useAuth()
    const [choice, setChoice] = useState("likes")
    const navigate = useNavigate()


    useEffect(() => {
        dispatch(fetchLikes());
        dispatch(fetchCollections());
    }, [dispatch]);

    const logOutButton = () => {
        dispatch(logOut())
        navigate("/")
    }

    const render = () => {
        if(choice==="likes"){
            return <Album photos={likedPhotos} />
        } else if (choice==="collections"){
            return <CollectionAlbum collections={collections}/>
        }
    }

    return (
        <BasePage pageName="profile">
            <div className="flex justify-between items-center">
                <h1>{user.username}</h1>
                <Button onClick={logOutButton} icon={<LogoutOutlined />}>Log out</Button>
            </div>
            <ChoiceLikesCollections choice={choice} setChoice={setChoice}/>
            {render()}
        </BasePage>
    );
};

export default ProfilePage;
