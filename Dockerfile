FROM nixos/nix:latest

# Install Python and dependencies
RUN nix-env -iA nixpkgs.python311 nixpkgs.python311Packages.pip nixpkgs.python311Packages.setuptools

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY golf_tracker/requirements.txt /app/golf_tracker/requirements.txt

# Create virtual environment and install dependencies
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r golf_tracker/requirements.txt

# Copy all files
COPY . /app/

# Set environment
ENV PATH="/opt/venv/bin:$PATH"

# Expose port
EXPOSE 5000

# Start command
WORKDIR /app/golf_tracker
CMD ["python3", "web_server.py"]
