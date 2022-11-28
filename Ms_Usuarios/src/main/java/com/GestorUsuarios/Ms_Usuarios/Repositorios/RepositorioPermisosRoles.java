package com.GestorUsuarios.Ms_Usuarios.Repositorios;

import com.GestorUsuarios.Ms_Usuarios.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
    @Query("{'rol.$id': ObjectId(?0), 'permiso.$id': ObjectId(?1)}")
    PermisosRoles getPermisosRoles(String id_rol, String id_permiso);
}
