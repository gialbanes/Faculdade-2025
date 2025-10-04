package br.com.faculdade.apidemo;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;

@RestController
@RequestMapping("/api/faculdade")
@Tag(name = "Faculdade", description = "Endpoints para informações da faculdade")
public class FaculdadeController {

    @GetMapping("/cursos")
    @Operation(summary = "Lista todos os cursos disponíveis")
    public List<String> getCursos() {
        return List.of("Desenvolvimento de Software Multiplataforma", "Gestão Empresarial", "Análise e Desenvolvimento de Sistemas");
    }

    @GetMapping("/alunos")
    @Operation(summary = "Lista alguns alunos matriculados")
    public List<String> getAlunos() {
        return List.of("Maria Silva", "João Santos", "Ana Pereira");
    }
}