import ChoiceButton from "./ChoiceButton";

const ChoiceLikesCollections = ({choice, setChoice}) => {
    const likesOnClick = () => {
        setChoice("likes")
    }

    const collectionsObClick = () => {
        setChoice("collections")
    }

    return (
        <div className="grid grid-cols-2 mb-2 gap-2">
            <ChoiceButton selected={choice === "likes"} onClick={likesOnClick}>Likes</ChoiceButton>
            <ChoiceButton selected={choice === "collections"} onClick={collectionsObClick}>Collections</ChoiceButton>
        </div>
    );
};

export default ChoiceLikesCollections;
