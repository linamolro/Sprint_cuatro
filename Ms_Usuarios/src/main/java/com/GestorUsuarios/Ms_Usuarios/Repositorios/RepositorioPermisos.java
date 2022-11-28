package com.GestorUsuarios.Ms_Usuarios.Repositorios;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Permisos;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermisos extends MongoRepository <Permisos, String> {
    @Query("{'url':?0,'metodo':?1}")
    Permisos getPermisos(String url, String metodo);
}
