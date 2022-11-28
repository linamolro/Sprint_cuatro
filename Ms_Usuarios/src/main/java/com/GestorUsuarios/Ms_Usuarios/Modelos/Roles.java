package com.GestorUsuarios.Ms_Usuarios.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document()

public class Roles {

    @Id
    private String id;
    private String tipo_rol;
    private String descripcion;

    public Roles(String tipo_rol, String descripcion) {
        this.tipo_rol = tipo_rol;
        this.descripcion = descripcion;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTipo_rol() {
        return tipo_rol;
    }

    public void setTipo_rol(String tipo_rol) {
        this.tipo_rol = tipo_rol;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}
