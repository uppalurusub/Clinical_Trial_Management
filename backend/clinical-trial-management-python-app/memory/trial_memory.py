from typing import Dict, Any, Optional
from threading import Lock
from datetime import datetime

from utils.logger import logger


class TrialMemory:
    """
    In-Memory Storage for Clinical Trial Management Platform

    Can be replaced with:
    - Redis
    - PostgreSQL
    - MongoDB
    - Azure Cosmos DB
    """

    def __init__(self):

        self.storage: Dict[str, Dict[str, Any]] = {}

        self.lock = Lock()

        logger.info(
            "TrialMemory initialized successfully"
        )

    def save(
        self,
        protocol_id: str,
        data: Dict[str, Any]
    ) -> bool:
        """
        Save trial execution result
        """

        try:

            with self.lock:

                self.storage[protocol_id] = {
                    "data": data,
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow()
                }

            logger.success(
                f"Protocol saved successfully: "
                f"{protocol_id}"
            )

            return True

        except Exception as ex:

            logger.exception(
                f"Failed to save protocol "
                f"{protocol_id}: {str(ex)}"
            )

            return False

    def get(
        self,
        protocol_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get protocol information
        """

        try:

            result = self.storage.get(protocol_id)

            if result:

                logger.info(
                    f"Protocol retrieved: "
                    f"{protocol_id}"
                )

            else:

                logger.warning(
                    f"Protocol not found: "
                    f"{protocol_id}"
                )

            return result

        except Exception as ex:

            logger.exception(
                f"Error retrieving protocol "
                f"{protocol_id}: {str(ex)}"
            )

            return None

    def update(
        self,
        protocol_id: str,
        data: Dict[str, Any]
    ) -> bool:
        """
        Update protocol data
        """

        try:

            with self.lock:

                if protocol_id not in self.storage:

                    logger.warning(
                        f"Protocol not found: "
                        f"{protocol_id}"
                    )

                    return False

                self.storage[protocol_id]["data"] = data

                self.storage[protocol_id][
                    "updated_at"
                ] = datetime.utcnow()

            logger.success(
                f"Protocol updated: "
                f"{protocol_id}"
            )

            return True

        except Exception as ex:

            logger.exception(
                f"Update failed for "
                f"{protocol_id}: {str(ex)}"
            )

            return False

    def delete(
        self,
        protocol_id: str
    ) -> bool:
        """
        Delete protocol
        """

        try:

            with self.lock:

                if protocol_id in self.storage:

                    del self.storage[protocol_id]

                    logger.success(
                        f"Protocol deleted: "
                        f"{protocol_id}"
                    )

                    return True

            logger.warning(
                f"Protocol not found: "
                f"{protocol_id}"
            )

            return False

        except Exception as ex:

            logger.exception(
                f"Delete failed for "
                f"{protocol_id}: {str(ex)}"
            )

            return False

    def get_all(self) -> Dict[str, Any]:
        """
        Get all trial records
        """

        try:

            logger.info(
                f"Returning "
                f"{len(self.storage)} protocols"
            )

            return self.storage

        except Exception as ex:

            logger.exception(
                f"Error fetching protocols: "
                f"{str(ex)}"
            )

            return {}

    def exists(
        self,
        protocol_id: str
    ) -> bool:
        """
        Check protocol existence
        """

        return protocol_id in self.storage

    def count(self) -> int:
        """
        Total protocols
        """

        return len(self.storage)

    def clear(self) -> bool:
        """
        Remove all protocols
        """

        try:

            with self.lock:

                self.storage.clear()

            logger.success(
                "All protocol records cleared"
            )

            return True

        except Exception as ex:

            logger.exception(
                f"Clear operation failed: "
                f"{str(ex)}"
            )

            return False

    def search(
        self,
        keyword: str
    ) -> Dict[str, Any]:
        """
        Search protocols
        """

        try:

            results = {}

            keyword = keyword.lower()

            for protocol_id, value in self.storage.items():

                if keyword in protocol_id.lower():

                    results[protocol_id] = value

                    continue

                if keyword in str(value).lower():

                    results[protocol_id] = value

            logger.info(
                f"Search completed. "
                f"Found {len(results)} records."
            )

            return results

        except Exception as ex:

            logger.exception(
                f"Search failed: {str(ex)}"
            )

            return {}

    def get_statistics(self) -> Dict[str, Any]:
        """
        Memory statistics
        """

        try:

            stats = {
                "total_protocols": len(
                    self.storage
                ),
                "memory_type": "InMemory",
                "status": "ACTIVE"
            }

            logger.info(
                f"Statistics generated: {stats}"
            )

            return stats

        except Exception as ex:

            logger.exception(
                f"Statistics generation failed: "
                f"{str(ex)}"
            )

            return {}