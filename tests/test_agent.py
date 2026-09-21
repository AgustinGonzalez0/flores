from flores.agent import Agent


def test_agent_tracks_memory_and_handles_tasks():
    agent = Agent(name="flores")

    result = agent.run("Summarize the meeting in one sentence.")

    assert isinstance(result, str)
    assert result
    assert len(agent.memory) >= 1
    assert agent.memory[-1]["task"] == "Summarize the meeting in one sentence."


def test_agent_formats_response_for_context():
    agent = Agent(name="flores")

    response = agent.respond("plan a project sprint")

    assert "plan a project sprint" in response.lower()
    assert "flores" in response.lower()
