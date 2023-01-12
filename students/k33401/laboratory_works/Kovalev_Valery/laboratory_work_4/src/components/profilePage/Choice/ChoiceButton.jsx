import React from 'react';
import {Button} from "antd";


const ChoiceButton = ({children, selected, onClick}) => {
    return (
        <Button onClick={onClick} className={`bg-transparent border-0 border-b-4 rounded-none ${selected && "border-sky-500"}`}>
            {children}
        </Button>
    );
};

export default ChoiceButton;
