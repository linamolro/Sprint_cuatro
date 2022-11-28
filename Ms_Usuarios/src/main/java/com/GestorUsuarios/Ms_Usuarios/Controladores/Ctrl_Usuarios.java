package com.GestorUsuarios.Ms_Usuarios.Controladores;

import com.GestorUsuarios.Ms_Usuarios.Modelos.Roles;
import com.GestorUsuarios.Ms_Usuarios.Modelos.Usuarios;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioRoles;
import com.GestorUsuarios.Ms_Usuarios.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

@CrossOrigin
@RestController
@RequestMapping("/usuarios")
public class Ctrl_Usuarios {
    @Autowired
    private RepositorioUsuario miRepositorioUsuario;
    @Autowired
    private RepositorioRoles miRepositorioRoles;

    @GetMapping("")
    public List<Usuarios> index(){
        return this.miRepositorioUsuario.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuarios create(@RequestBody Usuarios infoUsuario){
        infoUsuario.setCedula(infoUsuario.getCedula());
        infoUsuario.setUsername(infoUsuario.getUsername());
        infoUsuario.setEmail(infoUsuario.getEmail());
        infoUsuario.setPassword(convertirSHA256(infoUsuario.getPassword()));
        return this.miRepositorioUsuario.save(infoUsuario);
    }

    @GetMapping("{_id}")
    public Usuarios show(@PathVariable String _id){
        Usuarios useractual = this.miRepositorioUsuario
                .findById(_id)
                .orElse(null);
        return useractual;
    }

    @PutMapping("{_id}")
    public Usuarios update(@PathVariable String _id, @RequestBody Usuarios infoUsuario){
        Usuarios useractual=this.miRepositorioUsuario
                .findById(_id)
                .orElse(null);
        if (useractual != null) {
            useractual.setUsername(infoUsuario.getUsername());
            useractual.setEmail(infoUsuario.getEmail());
            useractual.setPassword(convertirSHA256(infoUsuario.getPassword()));
            return this.miRepositorioUsuario.save(useractual);
        }else {
            return null;
        }
    }
    /**
     *Asignacion del rol a los usuarios
     * @param id
     * @param id_rol
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}")
    public Usuarios asignarRolUsuario(@PathVariable String id, @PathVariable String id_rol){
        Usuarios userActual = this.miRepositorioUsuario
                .findById(id)
                .orElseThrow(RuntimeException::new);
        Roles rolActual = this.miRepositorioRoles
                .findById(id_rol)
                .orElseThrow(RuntimeException::new);
        if (userActual != null && rolActual!=null){
            userActual.setRol(rolActual);
            return this.miRepositorioUsuario.save(userActual);
        }else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{_id}")
    public void delete(@PathVariable String _id){
        Usuarios useractual = this.miRepositorioUsuario
                .findById(_id)
                .orElse(null);
        if(useractual!=null){
            this.miRepositorioUsuario.delete(useractual);
        }
    }
    public String convertirSHA256(String password){
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        }catch (NoSuchAlgorithmException e){
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b: hash){
            sb.append(String.format("%02x",b));
        }
        return sb.toString();
    }

    @PostMapping("/validar")
    public Usuarios validate(@RequestBody Usuarios infoUsuario, final HttpServletResponse response) throws IOException{
        Usuarios userActual = this.miRepositorioUsuario
                .getUserbyUsername(infoUsuario.getUsername());
        if(userActual != null && userActual.getPassword().equals(convertirSHA256(infoUsuario.getPassword()))){
            userActual.setPassword("");
            return userActual;
        }else{
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}
