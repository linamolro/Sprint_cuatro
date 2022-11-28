package com.GestorUsuarios.Ms_Usuarios.Controladores;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Roles;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioRoles;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class Ctrl_Roles {

    @Autowired
    private RepositorioRoles miRepositorioRoles;

    @GetMapping("")
    public List<Roles> index(){
        return this.miRepositorioRoles.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Roles create(@RequestBody Roles infoRoles){
        infoRoles.setTipo_rol(infoRoles.getTipo_rol());
        infoRoles.setDescripcion(infoRoles.getDescripcion());
        return this.miRepositorioRoles.save(infoRoles);
    }

    @GetMapping("{id}")
    public Roles show(@PathVariable String id){
        Roles rolUser = this.miRepositorioRoles
                .findById(id)
                .orElse(null);
        return rolUser;
    }

    @PutMapping("{id}")
    public Roles update(@PathVariable String id, @RequestBody Roles infoRoles){
        Roles rolActual = this.miRepositorioRoles
                .findById(id)
                .orElse(null);
        if (rolActual!=null){
            infoRoles.setTipo_rol(infoRoles.getTipo_rol());
            infoRoles.setDescripcion(infoRoles.getDescripcion());
            this.miRepositorioRoles.save(rolActual);
        }
        return null;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Roles rolActual = this.miRepositorioRoles
                .findById(id)
                .orElse(null);
        if (rolActual!=null){
            this.miRepositorioRoles.delete(rolActual);
        }
    }
}

