import React, {useState} from 'react';
import {Link} from "react-router-dom";
import {Button, Carousel, Image, Input, Modal} from "antd";
import {useDispatch} from "react-redux";
import {deleteCollection, updateCollection} from "../../../store/actions/profileActions";
import {CloseOutlined, DeleteOutlined, EditOutlined} from "@ant-design/icons";

const CollectionCard = ({collection}) => {
    const [visible, setVisible] = useState(false);
    const {title, photos} = collection
    const [current, setCurrent] = useState(0)
    const [changeTitle, setChangeTitle] = useState(false)
    const dispatch = useDispatch()

    const removePhotoFromCollection = () => {
        let photo_ids = photos.filter(e => e.photo_id !== photos[current].photo_id)
        photo_ids = photo_ids.map(e => e.photo_id)
        dispatch(updateCollection({collection_id: collection.id, photo_ids, title: collection.title}))
    }

    const removeCollection = () => {
        dispatch(deleteCollection({collection_id:collection.id}))
    }

    const changeCollectionTitle = (title) => {
        if(title.length>2){
            const photo_ids = collection.photos.map(e => e.photo_id)
            dispatch(updateCollection({collection_id: collection.id, photo_ids, title}))
            setChangeTitle(false)
        }
    }

    return (
        <div>
            <div key={title} style={{width: "100%", aspectRatio: "1/1"}}>
                <div className="flex justify-between items-center gap-2 mb-2">
                    {
                        changeTitle ? <Input onPressEnter={e=>{changeCollectionTitle(e.target.value)}} placeholder={title}/> : <h3 className="m-0  whitespace-nowrapyar">{title}</h3>
                    }

                    <div className="flex gap-2">
                        <Button onClick={()=>{setChangeTitle(!changeTitle)}} icon={changeTitle ? <CloseOutlined /> : <EditOutlined />}/>
                        <Button onClick={removeCollection} icon={<DeleteOutlined/>}></Button>
                    </div>
                </div>
                {photos.length ?
                    <>
                        <Carousel effect="fade">
                            <div
                                style={{
                                    width: "100%",
                                    aspectRatio: "1/1",
                                }}
                                key={photos[0].photo_image_url}
                            >
                                <Image
                                    preview={{visible: false}}
                                    style={{width: "100%", objectFit: "cover", aspectRatio: "1/1"}}
                                    src={`${photos[0].photo_image_url}?w=700`}
                                    onClick={() => {
                                        setVisible(true)
                                    }
                                    }
                                />
                            </div>

                        </Carousel>
                        <div style={{display: 'none', position: 'relative'}}>
                            <Image.PreviewGroup preview={{
                                visible,
                                onVisibleChange: (vis) => setVisible(vis),
                                countRender: (current, total) => {
                                    setCurrent(current - 1)
                                    return (<div className="flex gap-5 items-center">
                                        <Button onClick={removePhotoFromCollection} className="bg-transparent text-white">Remove
                                            from collection</Button>
                                        {current}/{total}
                                    </div>)
                                }
                            }}>
                                {photos.map(({photo_image_url}) => (
                                    <Image
                                        src={`${photo_image_url}`}
                                    />
                                ))}
                                <Button style={{position: "fixed", left: "50%", bottom: "50px", zIndex: "100"}}>Hello</Button>
                            </Image.PreviewGroup>
                        </div>
                    </> : <></>}
            </div>
        </div>
    );
};

export default CollectionCard;
