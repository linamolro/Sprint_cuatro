package com.GestorUsuarios.Ms_Usuarios.Controladores;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Permisos;
import com.GestorUsuarios.Ms_Usuarios.Modelos.PermisosRoles;
import com.GestorUsuarios.Ms_Usuarios.Modelos.Roles;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioPermisos;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioPermisosRoles;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioRoles;
import org.jetbrains.annotations.NotNull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class Ctrl_Permisos_Roles {
    @Autowired
    private RepositorioPermisosRoles miRepositorioPermisosRoles;
    @Autowired
    private RepositorioPermisos miRepositorioPermisos;
    @Autowired
    private RepositorioRoles miRepositorioRoles;

    @GetMapping("")
    public List<PermisosRoles> index(){
        return this.miRepositorioPermisosRoles.findAll();
    }

    /**
     *
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles create(@PathVariable String id_rol, @PathVariable String id_permiso){
        PermisosRoles nuevopermisorol = new PermisosRoles();
        Roles elrol = this.miRepositorioRoles
                .findById(id_rol).get();
        Permisos elpermiso = this.miRepositorioPermisos
                .findById(id_permiso).get();
        if(elrol != null && elpermiso != null){
            nuevopermisorol.setPermiso(elpermiso);
            nuevopermisorol.setRol(elrol);
            return this.miRepositorioPermisosRoles.save(nuevopermisorol);
        }else {
            return null;
        }
    }

    @GetMapping("{id}")
    PermisosRoles show(@PathVariable String id){
        PermisosRoles permisoRolActual = this.miRepositorioPermisosRoles
                .findById(id)
                .orElse(null);
        return permisoRolActual;
    }

    /**
     * @param id
     * @param id_rol
     * @param id_permisos
     */

    @PutMapping("{id}/rol/{id_rol}/permisos/{id_permisos}")
    public PermisosRoles update(@PathVariable String id, @PathVariable String id_rol, @PathVariable String id_permisos){
        PermisosRoles permisoRolActual = this.miRepositorioPermisosRoles
                .findById(id)
                .orElse(null);
        Roles elrol = this.miRepositorioRoles
                .findById(id_rol).get();
        Permisos elpermiso = this.miRepositorioPermisos
                .findById(id_permisos).get();
        if (permisoRolActual!=null && elpermiso!=null && elrol!=null){
            permisoRolActual.setPermiso(elpermiso);
            permisoRolActual.setRol(elrol);
            return this.miRepositorioPermisosRoles.save(permisoRolActual);
        }else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisosRoles permisoRolActual = this.miRepositorioPermisosRoles
                .findById(id)
                .orElse(null);
        if (permisoRolActual!=null){
            this.miRepositorioPermisosRoles.delete(permisoRolActual);
        }
    }

    @GetMapping("validar-permiso/rol/{id_rol}")
    public PermisosRoles getPermisos(@PathVariable String id_rol, @RequestBody Permisos infoPermiso){
        Permisos elPermiso = this.miRepositorioPermisos
                .getPermisos(infoPermiso.getUrl(),infoPermiso.getMetodo());
        Roles elRol = this.miRepositorioRoles.
                findById(id_rol).get();
        if(elPermiso!=null && elRol!=null){
            return this.miRepositorioPermisosRoles.getPermisosRoles(elRol.getId(), elPermiso.getId());
        }else{
            return null;
        }
    }
}
