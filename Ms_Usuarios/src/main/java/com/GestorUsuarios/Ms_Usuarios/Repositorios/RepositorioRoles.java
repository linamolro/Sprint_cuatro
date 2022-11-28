package com.GestorUsuarios.Ms_Usuarios.Repositorios;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Roles;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioRoles extends MongoRepository<Roles,String> {

}
