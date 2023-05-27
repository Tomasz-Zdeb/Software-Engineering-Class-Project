import React from 'react';
import {Col} from 'react-bootstrap';

const NoteItemComponent = ({
                               noteText,
                               setNoteText,
                               title,
                               setTitle,
                               catalogId,
                               setCatalogId,
                               description,
                               setDescription
                           }) => {
    const handleNoteChange = (event) => {
        const updatedNoteText = event.target.value;
        setNoteText(updatedNoteText);
    };

    const handleTitleChange = (event) => {
        const updatedTitle = event.target.value;
        setTitle(updatedTitle);
    };

    const handleCatalogIdChange = (event) => {
        const updatedCatalogId = event.target.value;
        setCatalogId(updatedCatalogId);
    };

    const handleDescriptionChange = (event) => {
        const updatedDescription = event.target.value;
        setDescription(updatedDescription);
    };

    return (
        <Col className="noteItem col-7 m-2 rounded">
            <div>
                <label>Tytuł:</label>
                <input type="text" value={title} onChange={handleTitleChange}/>
            </div>
            <div>
                <label>Identyfikator katalogu:</label>
                <input type="text" value={catalogId} onChange={handleCatalogIdChange}/>
            </div>
            <div>
                <label>Opis:</label>
                <input type="text" value={description} onChange={handleDescriptionChange}/>
            </div>
            <textarea
                className="note-text"
                value={noteText}
                onChange={handleNoteChange}
            />
        </Col>
    );
};

export default NoteItemComponent;
