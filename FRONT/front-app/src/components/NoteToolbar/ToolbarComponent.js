import React from 'react';
import {Button, Col} from 'react-bootstrap';
import {CloudDownload, CloudDownloadFill, Trash} from "react-bootstrap-icons";

const ToolbarComponent = ({handleSaveNewNote, handleSave, handleDeleteNote}) => {
    return (
        <Col className="rightbar col-2 m-2 rounded">
            <h3>Narzędzia</h3>
            <div className="toolbar">
                <Button className="m-2" onClick={handleSave}> <CloudDownloadFill size={24}
                                                                                 color="blue"/><br/>Zapisz <br/> notatkę</Button>
                <Button className="m-2" onClick={handleSaveNewNote}><CloudDownload size={24}
                                                                                   color="blue"/><br/>Zapisz
                    jako<br/>nową notatkę</Button>
                <Button className="m-2" variant="warning" onClick={handleDeleteNote}><Trash size={24}
                                                                                            color="black"/><br/>Usuń<br/> notatkę</Button>
            </div>
        </Col>
    );
};

export default ToolbarComponent;