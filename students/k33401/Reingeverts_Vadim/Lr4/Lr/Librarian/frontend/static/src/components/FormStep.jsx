import React from "react";
import { Box } from "@mantine/core";

import NonFieldErrors from "~/components/NonFieldErrors";

const FormStep = ({ nonFieldErrors, children }) => {
    return (
        <Box maw={340} mx="auto" mb="xs">
            <NonFieldErrors errors={nonFieldErrors} />
            {children}
        </Box>
    );
};

export default FormStep;
