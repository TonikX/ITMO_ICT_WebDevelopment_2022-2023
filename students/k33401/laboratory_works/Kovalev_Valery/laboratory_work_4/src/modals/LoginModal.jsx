import React, { useEffect } from 'react'
import { Modal, Form, Input, Button, Spin } from "antd";
import { useDispatch, useSelector } from 'react-redux';
import { login} from '../store/actions/authActions';

function LoginModal({isLoginModalOpen, setIsLoginModalOpen}) {

  const dispatch = useDispatch()

  const onLogin = ({username, password}) => {
    dispatch(login({username, password}))
  }

  const {isLoading, user} = useSelector(state=>state.auth)

  useEffect(()=>{
    if(user.username){
      setIsLoginModalOpen(false)
    }
  }, [setIsLoginModalOpen, user])
    
  return (
    <Modal title="Login" open={isLoginModalOpen} onOk={()=>{setIsLoginModalOpen(false)}} onCancel={()=>{setIsLoginModalOpen(false)}} footer={[]}>
      <Form
                    name="basic"
                    labelCol={{ span: 8 }}
                    wrapperCol={{ span: 16 }}
                    initialValues={{ remember: true }}
                    onFinish={onLogin}
                    autoComplete="off"
                >
                    <Form.Item
                        label="Username"
                        name="username"
                        rules={[{ required: true, message: 'Enter a username!' }]}
                    >
                        <Input/>
                    </Form.Item>



                    <Form.Item
                        label="Password"
                        name="password"
                        rules={[{ required: true, message: 'Enter a password!' }]}
                    >
                        <Input.Password />
                    </Form.Item>

                    <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                        <div className="flex gap-4 items-center">
                            <Button type="primary" htmlType="submit">
                                Log in
                            </Button>
                            {isLoading && <Spin/>}
                        </div>
                    </Form.Item>
                </Form>

      </Modal>
  )
}

export default LoginModal
