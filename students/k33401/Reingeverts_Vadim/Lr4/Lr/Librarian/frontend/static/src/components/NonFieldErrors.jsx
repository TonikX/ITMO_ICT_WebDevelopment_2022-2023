import React from "react";
import { Text } from "@mantine/core";

const NonFieldErrors = ({ errors }) => {
    return (
        <>
            {errors &&
                errors.map((nonFieldError, index) => (
                    <Text key={index} color="red">
                        {nonFieldError}
                    </Text>
                ))}
        </>
    );
};

export default NonFieldErrors;
