# BeMind AI SDK

A Python SDK for integrating AI capabilities into BeMind applications.

## Installation

```bash
pip install bemind-ai
```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/bemindlab/bmt-bemind-ai.git
cd bmt-bemind-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Usage

```python
from bemind_ai import BeMindAI

# Initialize the SDK
client = BeMindAI(api_key="your-api-key")

# Example usage
response = client.analyze_sentiment("I am feeling great today!")
print(response)
```

## Features

- Sentiment Analysis
- Text Generation
- Emotion Detection
- Mental Health Insights
- Conversation Analysis

## Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=bemind_ai
```

## Building and Publishing

```bash
# Build the package
python -m build

# Upload to PyPI (requires credentials)
python -m twine upload dist/*
```

## License

MIT License - see LICENSE file for details.