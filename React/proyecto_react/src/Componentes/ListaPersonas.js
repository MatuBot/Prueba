import React, { useEffect, useState } from "react";
import * as PerosonaServer from './PersonaServer';
import PersonasItem from "./PersonasItem";







const ListaPersonas = () => {

    const [personas, setPersonas] = useState([]);

    const listPersonas = async () => {
        try {
            const res = await PerosonaServer.listPersonas();
            const data = await res.json();
            setPersonas(data.personas);
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => {
        listPersonas();

    }, [])

    return (
        <div className="row">
            {personas.map((persona) => (
                <PersonasItem key={persona.id} persona={persona}/>
            ))}
        </div>
    );
}

export default ListaPersonas;
