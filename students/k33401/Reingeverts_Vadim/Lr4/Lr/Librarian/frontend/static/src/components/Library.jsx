import React, { useState } from "react";
import { Image, Text, Group } from "@mantine/core";

import imgUrl from "../../images/favicon-96.png";

const Library = () => {
    return (
        <>
            <Group position="center">
                <h1>hello world</h1>
                <Image width={200} height={120} src={imgUrl} />

                <Image
                    width={200}
                    height={120}
                    src={null}
                    alt="With default placeholder"
                    withPlaceholder
                />

                <Image
                    height={120}
                    width={200}
                    src="42.png"
                    alt="With custom placeholder"
                    withPlaceholder
                    placeholder={
                        <Text align="center">This image contained the meaning of life</Text>
                    }
                />
            </Group>
        </>
    );
};

export default Library;
