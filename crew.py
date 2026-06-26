from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()


def run_crew(sector: str) -> str:
    pesquisador = Agent(
        role="pesquisador de mercado",
        goal="Coletar informacoes importantes sobre {sector}",
        backstory="""
        Voce é um pesquisador experiente que analisa tendencias de mercado
        e fornece insights valiosos para empresas. Seu trabalho é garantir
        que todas as informacoes estejam atualizadas e bem documentadas.
        """,
        allow_delegation=False,
        verbose=True,
    )

    analista = Agent(
        role="analista de tendencias",
        goal="Interpretar dados e fornecer insights sobre o setor {sector} e identificar padroes e oportunidades",
        backstory="""
        Voce é um analista de mercado que analisa os dados coletados
        para identificar tendencias emergentes, oportunidades e ameacas no setor {sector}.
        """,
        allow_delegation=False,
        verbose=True,
    )

    redator = Agent(
        role="redator de relatorios",
        goal="Redigir relatorios sobre a analise de mercado do setor {sector}",
        backstory="""
        Voce é um redator experiente que cria conteudos informativos e persuasivos
        sobre o setor {sector}. Seu trabalho é comunicar insights de forma clara e impactante.
        """,
        allow_delegation=False,
        verbose=True,
    )

    coleta_dados = Task(
        description=(
            "1. Pesquisar e coletar informacoes atualizadas sobre o setor {sector}. "
            "2. Identificar principais players, tendencias e estatisticas do setor. "
            "3. Documentar todas as informacoes coletadas de forma organizada e clara."
        ),
        expected_output="Um relatorio detalhado contendo todas as informacoes coletadas sobre o setor {sector}",
        agent=pesquisador,
    )

    analise_tendencias = Task(
        description=(
            "1. Examinar os dados coletados pelo Pesquisador de Mercado. "
            "2. Identificar padroes, tendencias emergentes e oportunidades no setor {sector}. "
            "3. Elaborar uma analise detalhada destacando os principais pontos."
        ),
        expected_output="Um relatorio com insights e tendencias baseados nos dados do setor {sector}",
        agent=analista,
    )

    redacao_relatorio = Task(
        description=(
            "1. Usar a analise de tendencias para criar um relatorio detalhado sobre {sector}. "
            "2. Garantir que o relatorio seja bem estruturado e compreensivel. "
            "3. Apresentar um resumo executivo e recomendacoes finais."
        ),
        expected_output="Um relatorio de analise de mercado em formato Markdown, pronto para leitura e apresentacao.",
        agent=redator,
    )

    crew = Crew(
        agents=[pesquisador, analista, redator],
        tasks=[coleta_dados, analise_tendencias, redacao_relatorio],
        verbose=True,
    )

    resultado = crew.kickoff(inputs={"sector": sector})
    return str(resultado)
