import React, { memo, useEffect, useMemo, useState } from "react";
import useWindowSize from "../hooks/useWindowSize";
import PhotoCard from "./PhotoCard";

const splitElements = (n, array) => {
    const columns = [];
    const t_array = [...array];
    while (t_array.length) {
        for (let i = 0; i < n; i++) {
            if (!columns[i]) columns[i] = [];
            const elem = t_array.shift();
            if (elem) columns[i].push(elem);
        }
    }
    return columns;
};

const Album = ({ photos }) => {
    const [countOfColumns, setCountOfColumns] = useState(1);
    const windowSize = useWindowSize();
    const columns = useMemo(() => splitElements(countOfColumns, photos), [countOfColumns, photos]);

    useEffect(() => {
        if (windowSize[0] >= 997) {
            setCountOfColumns(3);
        } else if (windowSize[0] <= 997 && windowSize[0] >= 750) {
            setCountOfColumns(2);
        } else {
            setCountOfColumns(1);
        }
    }, [windowSize]);

    const getColumn = (photos, key) => {
        return (
            <div className="flex flex-col gap-2" key={key}>
                {photos.map((e) => {
                    return <PhotoCard key={e.photo_image_url} photo={e} />;
                })}
            </div>
        );
    };

    return <div className="flex gap-2">{columns.map((e, index) => getColumn(e, index))}</div>;
};

export default memo(Album);
