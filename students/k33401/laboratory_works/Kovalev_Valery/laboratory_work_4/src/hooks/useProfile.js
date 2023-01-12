import {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";
import {clearProfile} from "../store/slices/ProfileSlice";
import {fetchCollections, fetchLikes} from "../store/actions/profileActions";

export const useProfile = () => {
    const dispatch = useDispatch();
    const {user} = useSelector((state) => state.auth);
    useEffect(() => {
            if (user.username) {
                dispatch(fetchCollections())
                dispatch(fetchLikes())
            } else {
                dispatch(clearProfile())
            }
        },
        [dispatch, user])
}
