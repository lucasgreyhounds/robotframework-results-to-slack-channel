# Robot LA Notifications

RobotFrameworkLANotifications is a tool designed to send Robot Framework test results directly to a Slack channel. It helps teams stay updated on test outcomes in real-time, improving collaboration and visibility.

## Features

- Sends Robot Framework results to a specified Slack channel
- Customizable environment (`ENV`) input for flexible deployments
- Optional `footerText` input for personalized message footers

## Usage

1. **Configure Inputs:**
    - `ENV`: Specify the environment (e.g., `DEV`, `STG`).
    - `footerText`: (Optional) Add custom text to the message footer.

2. **Integrate with Your CI/CD Pipeline:**
    - Run your Robot Framework tests.
    - Trigger Robot LA Notifications with the required inputs.

## Example

```bash
python RobotFrameworkLANotifications.py --env=STG --footerText="Automated by CI"
```

## Requirements

- Python 3.x
- Access to Slack Webhook URL
- Robot Framework test results (XML or JSON)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/lucasgreyhounds/RobotFrameworkLANotifications
    ```

## Configuration

Set your Slack Webhook URL and other settings in the configuration file or as environment variables.

## License

MIT License

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.