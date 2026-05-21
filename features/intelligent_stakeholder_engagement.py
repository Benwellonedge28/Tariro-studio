
# intelligent_stakeholder_engagement.py
# TARIRO Studio: Intelligent Stakeholder Engagement & Communication

import datetime

class StakeholderManager:
    def __init__(self, stakeholders, communication_channels):
        self.stakeholders = self._parse_stakeholders(stakeholders)
        self.channels = communication_channels # e.g., {'email': ..., 'portal': ..., 'social': ...}
        self.engagement_logs = []
        print("Intelligent Stakeholder Engagement Manager initialized.")

    def _parse_stakeholders(self, stakeholders_data):
        parsed = {}
        for s in stakeholders_data:
            stakeholder_id = s.get("id") or s.get("name")
            if stakeholder_id:
                parsed[stakeholder_id] = {
                    "name": s.get("name"),
                    "type": s.get("type"), # e.g., 'investor', 'employee', 'customer', 'regulator'
                    "sentiment": s.get("sentiment", 0.5), # 0-1, 0.5 is neutral
                    "influence": s.get("influence", 0.5), # 0-1
                    "priority": s.get("priority", "medium"),
                    "last_engaged": None,
                    "preferences": s.get("preferences", {"frequency": "monthly", "channel": "email"})
                }
        return parsed

    def _analyze_sentiment(self, stakeholder_id):
        """
        Simulates sentiment analysis for a given stakeholder.
        In a real system, this would involve NLP on communications, social media, etc.
        """
        current_sentiment = self.stakeholders[stakeholder_id]["sentiment"]
        # Simulate a slight random fluctuation for demonstration
        new_sentiment = max(0, min(1, current_sentiment + (np.random.rand() - 0.5) * 0.1))
        self.stakeholders[stakeholder_id]["sentiment"] = new_sentiment
        return new_sentiment

    def _determine_message_tone_and_content(self, stakeholder_id, topic):
        """
        Determines the optimal tone and content for communication based on stakeholder profile.
        """
        stakeholder = self.stakeholders[stakeholder_id]
        sentiment = stakeholder["sentiment"]
        influence = stakeholder["influence"]

        tone = "neutral"
        if sentiment < 0.4: tone = "reassuring"
        elif sentiment > 0.7: tone = "optimistic"

        content_brief = f"Update on {topic} for {stakeholder['name']} (type: {stakeholder['type']})."
        if influence > 0.7: content_brief += " Emphasize strategic impact."
        if stakeholder["priority"] == "high": content_brief += " Include key metrics."

        print(f"  -> Determined tone: {tone}, content brief: {content_brief}")
        return {"tone": tone, "content_brief": content_brief}

    def engage_stakeholder(self, stakeholder_id, topic, force_channel=None):
        """
        Engages a specific stakeholder through their preferred or forced channel.
        """
        if stakeholder_id not in self.stakeholders:
            print(f"Stakeholder {stakeholder_id} not found.")
            return

        stakeholder = self.stakeholders[stakeholder_id]
        channel = force_channel or stakeholder["preferences"]["channel"]

        if channel not in self.channels:
            print(f"  Error: Communication channel '{channel}' not configured.")
            return

        message_details = self._determine_message_tone_and_content(stakeholder_id, topic)

        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "stakeholder_id": stakeholder_id,
            "topic": topic,
            "channel": channel,
            "tone": message_details["tone"],
            "content_brief": message_details["content_brief"],
            "initial_sentiment": stakeholder["sentiment"],
            "status": "sent"
        }
        self.engagement_logs.append(log_entry)
        self.stakeholders[stakeholder_id]["last_engaged"] = datetime.datetime.now()
        self._analyze_sentiment(stakeholder_id) # Simulate sentiment change after engagement

        print(f"Engaged {stakeholder['name']} ({stakeholder['type']}) on '{topic}' via {channel}.")
        print(f"  New sentiment for {stakeholder['name']}: {self.stakeholders[stakeholder_id]['sentiment']:.2f}")

    def run_engagement_cycle(self, topics_for_cycle, default_frequency="monthly"):
        """
        Runs a full engagement cycle, addressing all stakeholders based on their preferences.
        """
        print("--- Running Intelligent Stakeholder Engagement Cycle ---")
        for stakeholder_id, stakeholder in self.stakeholders.items():
            should_engage = False
            if stakeholder["last_engaged"] is None:
                should_engage = True # Engage new stakeholders immediately
            else:
                # Simulate frequency check
                if default_frequency == "monthly" and (datetime.datetime.now() - stakeholder["last_engaged"]).days > 30:
                    should_engage = True
                # Add more complex logic for different frequencies
            
            if should_engage:
                topic = np.random.choice(topics_for_cycle) # Choose a random topic for simplicity
                self.engage_stakeholder(stakeholder_id, topic)
            else:
                print(f"Skipping engagement for {stakeholder['name']}: already engaged recently.")
        print("--- Engagement Cycle Complete ---")

# Example usage:
if __name__ == "__main__":
    # Dummy data for demonstration
    sample_stakeholders = [
        {"name": "Investor Group A", "type": "investor", "sentiment": 0.6, "influence": 0.8, "priority": "high", "preferences": {"frequency": "quarterly", "channel": "portal"}},
        {"name": "Employee Council", "type": "employee", "sentiment": 0.7, "influence": 0.6, "priority": "medium", "preferences": {"frequency": "monthly", "channel": "email"}},
        {"name": "Key Customer XYZ", "type": "customer", "sentiment": 0.8, "influence": 0.7, "priority": "high", "preferences": {"frequency": "bi-weekly", "channel": "email"}},
        {"name": "Regulatory Body", "type": "regulator", "sentiment": 0.5, "influence": 0.9, "priority": "high", "preferences": {"frequency": "as_needed", "channel": "email"}},
    ]
    sample_channels = {"email": {"provider": "SMTP", "status": "active"}, "portal": {"provider": "Web", "status": "active"}}

    manager = StakeholderManager(sample_stakeholders, sample_channels)

    topics = ["Q4 Financial Results", "New Product Launch", "Company Culture Initiatives", "Regulatory Compliance Update"]
    manager.run_engagement_cycle(topics)

    # Manual engagement example
    manager.engage_stakeholder("Investor Group A", "Strategic Direction", force_channel="email")
