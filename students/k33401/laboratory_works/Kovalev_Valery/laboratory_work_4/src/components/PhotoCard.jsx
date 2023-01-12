import React, { useMemo } from "react";
import { HeartFilled, PlusSquareFilled } from "@ant-design/icons";
import { Card, Image } from "antd";
import { useDispatch, useSelector } from "react-redux";
import { likePhoto, unlikePhoto } from "../store/actions/profileActions";
import {openCollectionModal} from "../store/slices/CollectionModalSlice";

const getUsername = (username) => {
    if (username.length > 8) {
        return `@${username.slice(0, 8)}...`;
    } else {
        return `@${username}`;
    }
};
const PhotoCard = ({ photo }) => {
    const dispatch = useDispatch();
    const { likedPhotos } = useSelector((state) => state.profile);
    const liked = useMemo(() => {
        const ids = likedPhotos.map((e) => e.photo_id);
        return ids.includes(photo.photo_id);
    }, [likedPhotos, photo]);

    const onLike = () => {
        dispatch(likePhoto({ photo_id: photo.photo_id }));
    };

    const onUnlike = () => {
        dispatch(unlikePhoto({ photo_id: photo.photo_id }));
    };

    const addToCollection = () => {
        dispatch(openCollectionModal({photo}))
    }

    return (
        <Card
            cover={<Image src={`${photo.photo_image_url}?w=700`} preview={{ src: photo.photo_image_url }} />}
            actions={[
                <a
                    target="_blank"
                    href={`https://unsplash.com/@${photo.photographer_username}`}
                    style={{ textOverflow: "ellipsis" }}
                    rel="noreferrer"
                >
                    {getUsername(photo.photographer_username)}
                </a>,
                <HeartFilled
                    onClick={liked ? onUnlike : onLike}
                    style={liked ? { fontSize: "20px", color: "red" } : { fontSize: "20px" }}
                    key="like"
                />,
                <PlusSquareFilled onClick={addToCollection} style={{ fontSize: "20px" }} key="add" />,
            ]}
            type="inner"
            size="small"
            bodyStyle={{ display: "none" }}
        ></Card>
    );
};
export default PhotoCard;
