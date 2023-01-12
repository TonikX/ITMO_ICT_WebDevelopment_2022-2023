import React from "react";
import { Link } from "react-router-dom";
import { Carousel } from "antd";
import { AnimatePresence, motion } from "framer-motion";

const CategoriesAlbum = ({ categories, isLoading, countOnPage }) => {
    return (
        <AnimatePresence>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ delay: 0.5 }}
                className="grid grid-cols-1 gap-3 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4"
            >
                {isLoading ? (
                    <>
                        {Array(countOnPage)
                            .fill()
                            .map(() => (
                                <div className="aspect-square w-full animate-pulse bg-gray-300" />
                            ))}
                    </>
                ) : (
                    <>
                        {Object.entries(categories).map(([category, { photos, total }]) => (
                            <div key={category} style={{ width: "100%", aspectRatio: "1/1", position: "relative" }}>
                                <Link
                                    to={`/search/${category}`}
                                    style={{ width: "100%" }}
                                    className="w-100 absolute z-10 text-center text-xl font-light capitalize text-white backdrop-brightness-50"
                                >
                                    {category}
                                </Link>
                                <Carousel effect="fade">
                                    {photos.map(({ photo_image_url }) => (
                                        <div
                                            style={{
                                                width: "100%",
                                                aspectRatio: "1/1",
                                            }}
                                            key={photo_image_url}
                                        >
                                            <img
                                                style={{ width: "100%", objectFit: "cover", aspectRatio: "1/1" }}
                                                src={`${photo_image_url}?w=700`}
                                            />
                                        </div>
                                    ))}
                                </Carousel>
                            </div>
                        ))}
                    </>
                )}
            </motion.div>
        </AnimatePresence>
    );
};

export default CategoriesAlbum;
