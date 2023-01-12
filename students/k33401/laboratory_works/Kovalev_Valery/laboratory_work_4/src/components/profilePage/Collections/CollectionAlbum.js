import React from 'react';
import CollectionCard from "./CollectionCard";

const CollectionAlbum = ({collections}) => {
    return (
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4">
            {collections.map(
                collection => <CollectionCard collection={collection}/>
            )}
        </div>
    );
};

export default CollectionAlbum;
