import React, {useEffect} from 'react';
import {Col, Form, Row} from 'react-bootstrap';
import CKEditor from 'react-ckeditor-component';

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
        const updatedNoteText = event.editor.getData();
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

    useEffect(() => {
        // Aktualizacja zawartości CKEditor po zmianie noteText
        const editor = CKEditor.editorInstance;
        if (editor) {
            editor.setData(noteText);
        }
    }, [noteText]);


    const editorConfig = {
        styles: {
            height: '700px'
        }
    };


    return (
        <Col className="noteItem col-7 m-2 rounded">
            <Row>
                <Col className="col-4" style={{textAlign: 'center'}}>
                    <Row>
                        <label>Tytuł:</label>
                    </Row>
                    <Row className="m-1">
                        <Form.Control type="text" value={title} onChange={handleTitleChange}/>
                    </Row>
                </Col>
                <Col className="col-4" style={{textAlign: 'center'}}>
                    <Row>
                        <label>Nazwa katalogu:</label>
                    </Row>
                    <Row className="m-1">
                        <Form.Control type="text" value={catalogId} onChange={handleCatalogIdChange}/>
                    </Row>
                </Col>
                <Col className="col-4" style={{textAlign: 'center'}}>
                    <Row>
                        <label>Opis:</label>
                    </Row>
                    <Row className="m-1">
                        <Form.Control type="text" value={description} onChange={handleDescriptionChange}/>
                    </Row>
                </Col>
            </Row>
            <Row>
                <Col className="col-12 m-2 d-flex flex-column w-100">
                    <CKEditor
                        content={noteText}
                        events={{
                            change: handleNoteChange
                        }}
                        config={editorConfig}
                    />
                </Col>
            </Row>
        </Col>
    );
};

export default NoteItemComponent;