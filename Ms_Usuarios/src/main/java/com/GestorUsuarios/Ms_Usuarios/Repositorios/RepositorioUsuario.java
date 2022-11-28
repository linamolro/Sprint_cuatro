package com.GestorUsuarios.Ms_Usuarios.Repositorios;

import org.springframework.data.mongodb.repository.Query;
import com.GestorUsuarios.Ms_Usuarios.Modelos.Usuarios;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioUsuario extends MongoRepository<Usuarios,String> {
    @Query("{'username': ?0}")
    public Usuarios getUserbyUsername(String username);

}
