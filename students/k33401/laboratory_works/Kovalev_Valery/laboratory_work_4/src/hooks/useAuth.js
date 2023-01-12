import { useEffect, useMemo } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchUser } from "../store/actions/authActions";

export const useAuth = () => {
  const dispatch = useDispatch();
  const { token, user } = useSelector((state) => state.auth);
  const isAuth = useMemo(() => {
    return !!user?.username;
  }, [user]);

  useEffect(() => {
    if (!isAuth || !token) {
      dispatch(fetchUser());
    }
  }, [isAuth, dispatch]);

  return { user, isAuth };
};
