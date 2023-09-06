import React from "react";

const PersonasItem = ({ persona }) => {

    return (
        <div className="col-md-4 mb-4">
            <div className="card card-body">
                <h3 className="card-tittle">{persona.apellido}</h3>
                <p className="card-text">Nombre: <strong>{persona.nombre}</strong></p>
                <p className="card-text">Fecha de Nacimineto: <strong>{persona.fecha_nacimiento}</strong></p>
            </div>
        </div>
    )
}

export default PersonasItem;