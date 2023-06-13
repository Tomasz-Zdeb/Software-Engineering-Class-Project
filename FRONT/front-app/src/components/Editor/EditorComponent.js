import React, {useEffect, useState} from 'react';
import {Col, Container, Row} from 'react-bootstrap';
import NoteItemComponent from "../NoteItem/NoteItemComponent";
import ToolbarComponent from "../NoteToolbar/ToolbarComponent";
import NoteListComponent from "../NoteList/NoteListComponent";

const EditorComponent = ({token, setToken, setIsLoggedIn}) => {
    const [noteText, setNoteText] = useState('Wprowadź treść notatki');
    const [title, setTitle] = useState('');
    const [catalogId, setCatalogId] = useState('');
    const [description, setDescription] = useState('');
    const [actualNoteID, setActualNoteID] = useState(0);
    const [noteData, setNoteData] = useState(null);

    const handleLogout = () => {
        setIsLoggedIn(false);
        setToken('');
        localStorage.removeItem('token');
        window.location.reload();
    };

    const fetchData = async () => {
        try {
            const url = "http://localhost:5000/notes";
            const response = await fetch(url, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                }
            });
            const data = await response.json();
            setNoteData(data);
        } catch (error) {
            console.error(error);
        }
    };

    const handleSaveNewNote = async () => {
        const url = 'http://localhost:5000/note';
        const noteData = {
            title: title,
            catalog_name: catalogId,
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

            await fetchData();

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
            catalog_name: catalogId,
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

            await fetchData();

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
                fetchData();

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


    const handleNoteClick = async (note) => {
        try {
            const url = `http://localhost:5000/note?note_id=${note.note_id}`;
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            });
            if (response.ok) {
                const data = await response.json();
                setActualNoteID(note.note_id);
                setTitle(note.title);
                setCatalogId(note.catalog_name);
                setDescription(note.description);
                setNoteText(data.body);
            } else {
                console.error('Failed to fetch note:', response.status);
            }
        } catch (error) {
            console.error(error);
        }
    };


    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div className="app">
            <Container fluid>
                <Row>
                    <Col className="topbar col-12 m-1 rounded"><h1>Notatnik</h1></Col>
                </Row>
                <Row className="mt-3">
                    {noteData ? (
                        <NoteListComponent noteData={noteData} handleNoteClick={handleNoteClick}/>
                    ) : (
                        <p>Ładowanie danych...</p>
                    )}
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
                    <ToolbarComponent
                        handleSave={handleSave}
                        handleSaveNewNote={handleSaveNewNote}
                        handleDeleteNote={handleDeleteNote}
                        handleLogout={handleLogout}
                    />
                </Row>
            </Container>
        </div>
    );
};

export default EditorComponent;
