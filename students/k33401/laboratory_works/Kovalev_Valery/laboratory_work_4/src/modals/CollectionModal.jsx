import React, {useEffect, useState} from 'react';
import {Button, Input, Modal, Select} from "antd";
import {useDispatch, useSelector} from "react-redux";
import {closeCollectionModal} from "../store/slices/CollectionModalSlice";
import {createCollection, fetchCollections, updateCollection} from "../store/actions/profileActions";

const CollectionModal = () => {
    const dispatch = useDispatch()
    const {open, selectedPhoto} = useSelector(state => state.collectionModal)
    const {collections} = useSelector(state => state.profile)
    const [selectedCollectionId, setSelectedCollectionId] = useState(-1)
    const [collectionTitle, setCollectionTitle] = useState("")
    const [addCollection, setAddCollection] = useState(false)
    const close = () => {
        dispatch(closeCollectionModal())
    }

    const onSelect = (collection_id) => {
        setSelectedCollectionId(collection_id)
    }

    useEffect(() => {
        if (open) {
            setAddCollection(false)
            dispatch(fetchCollections())
        }
    }, [dispatch, open])

    const onFinish = () => {
        if(addCollection){
            dispatch(createCollection({title:collectionTitle, photo_ids: [selectedPhoto.photo_id]}))
            dispatch(closeCollectionModal())
        } else {
            const selectedCollection = collections.find(e => (e.id === selectedCollectionId))
            const photo_ids = [...selectedCollection.photos.map(e => (e.photo_id)), selectedPhoto.photo_id]
            dispatch(updateCollection({collection_id: selectedCollectionId, photo_ids, title: selectedCollection.title}))
            dispatch(closeCollectionModal())
        }
    }

    const onAdd = () => {
        setAddCollection(!addCollection)
    }


    return (
        <Modal
            open={open}
            title="Collections"
            onOk={close}
            onCancel={close}
            footer={[
                <Button key="submit" type="primary" onClick={onFinish}>
                    Add to this collection
                </Button>,
            ]}
        >
            <>
                {
                    addCollection ?
                        <div className="flex gap-2">
                            <Input onChange={e=>{setCollectionTitle(e.target.value)}} placeholder="Enter title"/>
                        </div>
                        :
                        <div className="flex gap-2">
                            <Select onSelect={onSelect} placeholder="Select collection" className="w-full">
                                {collections.map(e => (
                                    <Select.Option value={e.id}>{e.title}</Select.Option>
                                ))}
                            </Select>
                            <Button onClick={onAdd}>New</Button>
                        </div>
                }
            </>

        </Modal>
    );
};

export default CollectionModal;
