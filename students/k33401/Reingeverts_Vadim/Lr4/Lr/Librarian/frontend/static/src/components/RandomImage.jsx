import React from "react";
import { Image, AspectRatio } from "@mantine/core";

import chooseWeightedIndex from "~/utils/ChooseRandom";

const RandomImage = ({ srcSet, seed, alt = "" }) => {
    const choice = chooseWeightedIndex(srcSet, seed);
    const randomSrc = srcSet[choice];

    return (
        <AspectRatio ratio={9 / 9}>
            <Image withPlaceholder src={randomSrc} alt={alt} />
        </AspectRatio>
    );
};

export default RandomImage;
