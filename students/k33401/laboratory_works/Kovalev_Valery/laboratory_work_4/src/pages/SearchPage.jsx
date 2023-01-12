import React, { useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import BasePage from "./BasePage/BasePage";
import { Input, Select } from "antd";
import { fetchSearchPhotos, setKeywords, setTone } from "../store/actions/searchActions";
import { useDispatch, useSelector } from "react-redux";
import Album from "../components/Album";
import { useInView } from "react-intersection-observer";

const { Search } = Input;

const toneOptions = [
    {
        value: "red",
        label: "Red",
    },
    {
        value: "blue",
        label: "Blue",
    },
    {
        value: "green",
        label: "Green",
    },
    {
        value: "magenta",
        label: "Magenta",
    },
    {
        value: "yellow",
        label: "Yellow",
    },
    {
        value: "cyan",
        label: "Cyan",
    },
];

const SearchPage = () => {
    const { category, tone } = useParams();
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const { photos, keywords, searchWord, isLoading, count, offset, searchTone } = useSelector((state) => state.search);
    const { ref, inView } = useInView();

    const onSearch = (value) => {
        if (tone && value) {
            navigate(`/search/${value}/${tone}`);
        } else {
            navigate(`/search/${value}`);
        }
    };

    const onChangeTone = (value) => {
        if (category && value) {
            navigate(`/search/${category}/${value}`);
        } else if (category && !value) {
            navigate(`/search/${category}`);
        }
    };

    useEffect(() => {
        if (keywords.length && !photos.length) {
            dispatch(fetchSearchPhotos());
        }
    }, [dispatch, keywords, searchTone]);

    useEffect(() => {
        if (inView && photos.length && !isLoading && offset < count && offset > 0) {
            dispatch(fetchSearchPhotos());
        }
    }, [isLoading, dispatch, photos, inView, offset, count]);

    useEffect(() => {
        if (searchWord !== category) {
            dispatch(setKeywords(category));
        }
    }, [dispatch, category, searchWord]);

    useEffect(() => {
        if (tone !== searchTone) {
            dispatch(setTone(tone));
        }
    }, [dispatch, searchTone, tone]);

    return (
        <BasePage pageName="search">
            <div>
                <div className="flex mb-2">
                    <Search placeholder="Search" onSearch={onSearch} defaultValue={category} />
                    <Select
                        allowClear
                        value={tone}
                        placeholder="Tone"
                        onChange={onChangeTone}
                        style={{ width: 120 }}
                        defaultValue={tone}
                        options={toneOptions}
                    />
                </div>
                <div className="relative">
                    <Album photos={photos} />
                    <div
                        ref={ref}
                        style={{ height: "30%", width: "100%", position: "absolute", bottom: 0, left: 0, zIndex: -10 }}
                    >
                        sdfsdf
                    </div>
                </div>
            </div>
        </BasePage>
    );
};

export default SearchPage;
