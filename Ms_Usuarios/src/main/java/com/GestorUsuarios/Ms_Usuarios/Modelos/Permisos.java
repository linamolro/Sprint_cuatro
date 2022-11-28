package com.GestorUsuarios.Ms_Usuarios.Modelos;

public class Permisos {

    private String id;

    private String url;

    private String metodo;

    public Permisos(String url, String metodo) {
        this.url = url;
        this.metodo = metodo;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getMetodo() {
        return metodo;
    }

    public void setMetodo(String metodo) {
        this.metodo = metodo;
    }
}
