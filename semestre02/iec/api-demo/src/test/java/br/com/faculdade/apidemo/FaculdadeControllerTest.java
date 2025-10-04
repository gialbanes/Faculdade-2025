package br.com.faculdade.apidemo;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class FaculdadeControllerTest {

    @Autowired
    private FaculdadeController controller;

    @Test
    void contextLoads() {
        // Teste simples para garantir que o controller foi injetado e não é nulo
        assertThat(controller).isNotNull();
    }

    @Test
    void deveRetornarTresCursos() {
        // Teste que verifica se a lista de cursos tem 3 itens
        assertThat(controller.getCursos()).hasSize(3);
    }

    @Test
    void deveRetornarNomeDeAlunoEspecifico() {
        // Teste que verifica se "João Santos" está na lista de alunos
        assertThat(controller.getAlunos()).contains("João Santos");
    }
}