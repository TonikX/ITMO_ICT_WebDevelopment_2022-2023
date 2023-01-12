import { useEffect, useState } from "react";

const getWindowSize = () => {
    return [window.innerWidth, window.innerHeight];
};

export const useWindowSize = () => {
    const [windowSize, setWindowSize] = useState(getWindowSize());

    useEffect(() => {
        function handleWindowResize() {
            setWindowSize(getWindowSize());
        }

        window.addEventListener("resize", handleWindowResize);

        return () => {
            window.removeEventListener("resize", handleWindowResize);
        };
    }, []);

    return windowSize;
};

export default useWindowSize;
