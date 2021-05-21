from uses_services.platform_ import Platform


class ServiceMissingError(Exception):
    """Error raised when a test uses a service but that service is missing."""
    # TODO add special platform handling to DRY instructions across services

    def __init__(self, service, platform: Platform, instructions="", msg=None):
        if msg is None:
            msg = f"The {service} service does not seem to be running or is not accessible!"
            if instructions:
                msg += f"\n{instructions}"
        super().__init__(msg)
        self.service = service
        self.platform = platform
        self.instructions = instructions
