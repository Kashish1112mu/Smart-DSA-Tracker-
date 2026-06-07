def get_ai_suggestions(problems):
    topic_stats = {}

    for p in problems:
        topic = p[2]
        status = p[3]
        attempts = p[6] if p[6] else 0

        if topic not in topic_stats:
            topic_stats[topic] = {
                "unsolved": 0,
                "attempts": 0
            }

        if status == "Not Solved":
            topic_stats[topic]["unsolved"] += 1

        topic_stats[topic]["attempts"] += attempts

    sorted_topics = sorted(
        topic_stats.items(),
        key=lambda x: (x[1]["unsolved"], x[1]["attempts"]),
        reverse=True
    )

    recommendations = []

    for topic, stats in sorted_topics[:5]:
        recommendations.append(
            f"Focus on {topic}: {stats['unsolved']} unsolved, {stats['attempts']} total attempts"
        )

    return recommendations


def next_best_problem(problems):
    if not problems:
        return "Add some problems first."

    worst_topic = None
    max_weight = -1

    for p in problems:
        topic = p[2]
        status = p[3]
        attempts = p[6] if p[6] else 0

        weight = 0

        if status == "Not Solved":
            weight += 3

        if attempts > 2:
            weight += 2

        if weight > max_weight:
            max_weight = weight
            worst_topic = topic

    return f"Next best topic to practice: {worst_topic}"