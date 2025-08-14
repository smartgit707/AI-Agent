 {json.dumps(personas_data, indent=2)}

        For each persona, create a campaign with:
        1. Campaign title and theme
        1. Campaign title and central theme (memorable tagline)
        2. Core messaging strategy
        3. Channel recommendations
        4. Content strategy
        5. ROI predictions
        6. Success metrics

        Return as JSON with a "campaigns" array. No markdown formatting.
        Return as JSON with a "campaigns" array. Each campaign must include:
        - title
        - theme (catchy campaign theme/tagline)
        - persona_target
        - key_message
        - value_propositions (array)
        - channels (array)
        - content_strategy (array)
        - predicted_roi
        - confidence_interval
 
        No markdown formatting.
        """

        
        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
@@ -1421,7 +1433,14 @@ def display_campaigns(campaigns_data):
        persona_target = campaign.get('persona_target', 'Target Audience')
        theme = campaign.get('theme')
        if not theme:
            theme = campaign.get('campaign_theme', 'Campaign Theme')
            theme = campaign.get('campaign_theme') 
            if not theme:
        # Check if theme is nested in other fields
                messaging = campaign.get('core_messaging', {})
                if isinstance(messaging, dict):
                    theme = messaging.get('theme', 'Campaign Theme')
                else:
                    theme = 'Campaign Theme'

        key_message = campaign.get('key_message')
        if not key_message:
