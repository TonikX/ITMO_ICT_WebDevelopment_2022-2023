import React, {useEffect} from 'react'
import {Button, Form, Input, Modal, Spin} from "antd"
import {useDispatch, useSelector} from "react-redux";
import {register} from "../store/actions/authActions";

function RegisterModal({isRegisterModalOpen, setIsRegisterModalOpen}) {

    const dispatch = useDispatch()

    const onFinish = ({username, password}) => {
        dispatch(register({username, password}))
    }

    const {isLoading, user} = useSelector(state=>state.auth)

    useEffect(()=>{
        if(user.username){
            setIsRegisterModalOpen(false)
        }
    }, [setIsRegisterModalOpen, user])

    return (
        <Modal title="Register" open={isRegisterModalOpen} onOk={() => {
            setIsRegisterModalOpen(false)
        }} onCancel={() => {
            setIsRegisterModalOpen(false)
        }} footer={[]}>
            <Form
                name="basic"
                labelCol={{span: 8}}
                wrapperCol={{span: 16}}
                initialValues={{remember: true}}
                onFinish={onFinish}
                autoComplete="off"
            >
                <Form.Item
                    label="Username"
                    name="username"
                    rules={[{required: true, message: 'Enter a username!'}]}
                >
                    <Input/>
                </Form.Item>


                <Form.Item
                    label="Password"
                    name="password"
                    rules={[{required: true, message: 'Enter a password!'}]}
                >
                    <Input.Password/>
                </Form.Item>

                <Form.Item wrapperCol={{offset: 8, span: 16}}>
                    <div className="flex gap-4 items-center">
                        <Button type="primary" htmlType="submit">
                            Register
                        </Button>
                        {isLoading && <Spin/>}
                    </div>
                </Form.Item>
            </Form>

        </Modal>
    )
}

RegisterModal.propTypes = {}

export default RegisterModal
