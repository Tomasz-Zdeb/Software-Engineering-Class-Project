import React, {useState} from 'react';
import {Col, Container, Row} from 'react-bootstrap';
import NoteItemComponent from "../NoteItem/NoteItemComponent";
import ToolbarComponent from "../NoteToolbar/ToolbarComponent";

const EditorComponent = ({token}) => {
    const [noteText, setNoteText] = useState('Wprowadź treść notatki');
    const [title, setTitle] = useState('');
    const [catalogId, setCatalogId] = useState('1');
    const [description, setDescription] = useState('');
    const [actualNoteID, setActualNoteID] = useState(0);

    const handleSaveNewNote = async () => {
        const url = 'http://localhost:5000/note';
        const noteData = {
            title: title,
            catalog_id: catalogId,
            description: description,
            body: noteText
        };

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(noteData)
            });

            if (response.status === 201) {
                const responseData = await response.json();
                const noteId = responseData.note_id;
                setActualNoteID(noteId);
                alert('Zapisano nową notatkę. ID:' + noteId);
            } else if (response.status === 400) {
                console.error('Błędne żądanie');
            } else if (response.status === 401) {
                console.error('Brak autoryzacji');
            } else if (response.status === 404) {
                console.error('Użytkownik lub katalog nie został znaleziony');
            } else if (response.status === 422) {
                console.error('Nieprawidłowy token');
            } else {
                console.error('Wystąpił błąd podczas zapisywania notatki');
            }
        } catch (error) {
            console.error('Wystąpił błąd podczas wysyłania żądania', error);
        }
    };

    const handleSave = async () => {
        const url = 'http://localhost:5000/note';
        if (actualNoteID == null || actualNoteID === 0) {
            alert("Najpierw zapisz jako nową notatkę");
            return;
        }
        const noteData = {
            note_id: actualNoteID,
            title: title,
            catalog_id: catalogId,
            description: description,
            body: noteText
        };

        try {
            const response = await fetch(url, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(noteData)
            });

            if (response.status === 201) {
                console.log('Notatka została zapisana');
            } else if (response.status === 400) {
                console.error('Błędne żądanie');
            } else if (response.status === 401) {
                console.error('Brak autoryzacji');
            } else if (response.status === 404) {
                console.error('Użytkownik lub katalog nie został znaleziony');
            } else if (response.status === 422) {
                console.error('Nieprawidłowy token');
            } else {
                console.error('Wystąpił błąd podczas zapisywania notatki');
            }
        } catch (error) {
            console.error('Wystąpił błąd podczas wysyłania żądania', error);
        }
    };

    const handleDeleteNote = () => {
        if (actualNoteID == null || actualNoteID === 0) {
            alert("Najpierw zapisz jako nową notatkę");
            return;
        }

        fetch(`http://localhost:5000/note?note_id=${actualNoteID}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`,
            },
        })
            .then(response => {
                if (response.status === 200) {
                    alert('Notatka została usunięta.');
                    setActualNoteID(0);
                } else if (response.status === 401) {
                    console.error('Brak autoryzacji.');
                } else if (response.status === 403) {
                    console.error('Brak dostępu. Zabronione.');
                } else if (response.status === 404) {
                    console.error('Notatka nie znaleziona.');
                } else if (response.status === 422) {
                    console.error('Nieprawidłowy token.');
                } else {
                    console.error('Wystąpił nieznany błąd.');
                }
            })
            .catch(error => {
                console.error('Błąd podczas usuwania notatki:', error);
            });
    };


    return (
        <div className="app">
            <Container fluid>
                <Row>
                    <Col className="topbar col-12 m-1 rounded"><h1>Notatnik</h1></Col>
                </Row>
                <Row className="mt-3">
                    <Col className="leftbar col-2 m-2 rounded">Eksplorator notatek</Col>
                    <NoteItemComponent
                        token={token}
                        noteText={noteText}
                        setNoteText={setNoteText}
                        title={title}
                        setTitle={setTitle}
                        catalogId={catalogId}
                        setCatalogId={setCatalogId}
                        description={description}
                        setDescription={setDescription}
                    />
                    <ToolbarComponent handleSave={handleSave} handleSaveNewNote={handleSaveNewNote}
                                      handleDeleteNote={handleDeleteNote}/>
                </Row>
            </Container>
        </div>
    );
};

export default EditorComponent;
