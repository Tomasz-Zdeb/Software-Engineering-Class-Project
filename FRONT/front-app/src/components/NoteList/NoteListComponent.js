import React from "react";
import {Col, ListGroup} from "react-bootstrap";
import {Folder, Newspaper, Pencil} from "react-bootstrap-icons";

const NoteListComponent = ({noteData, handleNoteClick}) => {
    const renderNotes = (notes) => {
        return notes.map((note) => (
            <ListGroup.Item key={note.note_id} onClick={() => handleNoteClick(note)}>
                <h5 className="text-sm">{note.title || "Brak nazwy"}</h5>
                {note.description && (
                    <p className="text-sm">
                        <Newspaper/> {note.description}
                    </p>
                )}
                <p className="text-sm"><Pencil/> {note.updated_date}</p>
            </ListGroup.Item>
        ));
    };

    const renderCatalog = (catalog) => {
        const {catalog_name, catalog_id, notes, subcatalogs} = catalog;
        return (
            <ListGroup.Item key={catalog_id}>
                <h4 className="small">
                    {catalog_name ? (
                        <>
                            <Folder/> {catalog_name}
                        </>
                    ) : (
                        <>
                            <Folder/> /
                        </>
                    )}
                </h4>
                {notes && notes.length > 0 ? (
                    <ListGroup variant="flush">{renderNotes(notes)}</ListGroup>
                ) : (
                    <p>Brak notatek w tym katalogu.</p>
                )}
                {subcatalogs && subcatalogs.length > 0 && (
                    <ListGroup variant="flush">
                        {subcatalogs.map((subcatalog) => renderCatalog(subcatalog))}
                    </ListGroup>
                )}
            </ListGroup.Item>
        );
    };

    const renderUncatalogedNotes = (uncatalogedNotes) => {
        return (
            <ListGroup variant="flush">
                {uncatalogedNotes && uncatalogedNotes.length > 0 ? (
                    renderNotes(uncatalogedNotes)
                ) : (
                    <p>-</p>
                )}
            </ListGroup>
        );
    };

    return (
        <Col className="rightbar col-2 m-2 rounded overflow-auto">
            <h3>Notatki</h3>
            <ListGroup variant="flush" className="m-1">
                {noteData &&
                    noteData.catalogs &&
                    noteData.catalogs.length > 0 &&
                    noteData.catalogs.map((catalog) => renderCatalog(catalog))}
                {noteData && noteData.uncataloged && (
                    <>{renderUncatalogedNotes(noteData.uncataloged)}</>
                )}
            </ListGroup>
        </Col>
    );
};

export default NoteListComponent;
