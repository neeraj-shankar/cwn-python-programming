import pytest
from my_app.samples.cloud_service import upload_system_log

def test_upload_success(monkeypatch, mocker):
    # 1. MONKEYPATCH the environment
    # This ensures os.getenv("LOG_BUCKET") returns our fake string
    monkeypatch.setenv("LOG_BUCKET", "test-bucket-123")
    
    # 2. MOCKER the external dependency
    # We patch the 'boto3.client' inside our target module
    mock_s3 = mocker.patch("cloud_service.boto3.client")
    
    # Define what the mock client should look like
    mock_client_instance = mock_s3.return_value
    
    # 3. ACT
    result = upload_system_log("local_file.txt")
    
    # 4. ASSERT
    assert result is True
    
    # Verify the environment was used correctly in the API call
    mock_client_instance.upload_file.assert_called_once_with(
        "local_file.txt", 
        "test-bucket-123",  # This came from monkeypatch!
        "logs/latest.log"
    )