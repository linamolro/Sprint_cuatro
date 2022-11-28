package com.GestorUsuarios.Ms_Usuarios.Controladores;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Permisos;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioPermisos;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class Ctrl_Permisos {
    @Autowired
    private RepositorioPermisos miRepositorioPermisos;

    @GetMapping("")
    public List<Permisos> index(){
        return this.miRepositorioPermisos.findAll();
    }

    @PostMapping
    public Permisos create(@RequestBody Permisos infoPermisos){
        infoPermisos.setUrl(infoPermisos.getUrl());
        infoPermisos.setMetodo(infoPermisos.getMetodo());
        return this.miRepositorioPermisos.save(infoPermisos);
    }

    @GetMapping("{id}")
    public Permisos show(@PathVariable String id){
        Permisos permisoActual = this.miRepositorioPermisos
                .findById(id)
                .orElse(null);
        return permisoActual;
    }

    @PutMapping("{id}")
    public Permisos update(@PathVariable String id, @RequestBody Permisos infoPermisos){
        Permisos permisoActual = this.miRepositorioPermisos
                .findById(id)
                .orElse(null);
        if(permisoActual != null){
            permisoActual.setMetodo(infoPermisos.getMetodo());
            return this.miRepositorioPermisos.save(permisoActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Permisos permisoActual = this.miRepositorioPermisos
                .findById(id)
                .orElse(null);
        if (permisoActual != null){
            this.miRepositorioPermisos.delete(permisoActual);
        }
    }
}
