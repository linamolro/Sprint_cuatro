package com.GestorUsuarios.Ms_Usuarios.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class PermisosRoles {
    @Id
    private String id;
    @DBRef
    private Roles rol;
    @DBRef
    private Permisos permiso;

    public PermisosRoles(){
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Roles getRol() {
        return rol;
    }

    public void setRol(Roles rol) {
        this.rol = rol;
    }

    public Permisos getPermiso() {
        return permiso;
    }

    public void setPermiso(Permisos permiso) {
        this.permiso = permiso;
    }
}
