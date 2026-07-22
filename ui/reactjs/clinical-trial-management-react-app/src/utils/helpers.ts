
/**
 * ==========================================================
 * Clinical Trial Management System
 * Helper Functions
 * ==========================================================
 */

/**
 * Format Date
 */
export const formatDate = (
  date: string | Date
): string => {
  return new Date(date).toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
};

/**
 * Format Date & Time
 */
export const formatDateTime = (
  date: string | Date
): string => {
  return new Date(date).toLocaleString("en-IN");
};

/**
 * Format Number
 */
export const formatNumber = (
  value: number
): string => {
  return value.toLocaleString("en-IN");
};

/**
 * Format Currency
 */
export const formatCurrency = (
  amount: number
): string => {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 2,
  }).format(amount);
};

/**
 * Calculate Enrollment Percentage
 */
export const calculateEnrollmentPercentage = (
  enrolled: number,
  planned: number
): number => {
  if (planned === 0) return 0;

  return Number(
    ((enrolled / planned) * 100).toFixed(2)
  );
};

/**
 * Calculate Progress
 */
export const calculateProgress = (
  completed: number,
  total: number
): number => {
  if (total === 0) return 0;

  return Math.round(
    (completed / total) * 100
  );
};

/**
 * Capitalize First Letter
 */
export const capitalize = (
  value: string
): string => {
  if (!value) return "";

  return value.charAt(0).toUpperCase() +
         value.slice(1).toLowerCase();
};

/**
 * Truncate Text
 */
export const truncateText = (
  text: string,
  length = 50
): string => {
  if (text.length <= length)
    return text;

  return `${text.substring(0, length)}...`;
};

/**
 * Bootstrap Badge Color
 */
export const getStatusBadge = (
  status: string
): string => {

  switch (status.toLowerCase()) {

    case "active":
      return "success";

    case "completed":
      return "primary";

    case "recruiting":
      return "info";

    case "planned":
      return "secondary";

    case "suspended":
      return "warning";

    case "terminated":
      return "danger";

    default:
      return "dark";
  }
};

/**
 * Random UUID
 */
export const generateId = (): string => {
  return crypto.randomUUID();
};

/**
 * Sleep Utility
 */
export const sleep = (
  milliseconds: number
): Promise<void> => {

  return new Promise(resolve =>
    setTimeout(resolve, milliseconds)
  );

};

/**
 * Search Objects
 */
export const searchTrials = <T>(
  items: T[],
  keyword: string
): T[] => {

  if (!keyword)
    return items;

  const search = keyword.toLowerCase();

  return items.filter(item =>
    JSON.stringify(item)
      .toLowerCase()
      .includes(search)
  );
};

/**
 * Sort Objects
 */
export const sortByField = <T>(
  items: T[],
  field: keyof T,
  ascending = true
): T[] => {

  return [...items].sort((a, b) => {

    if (a[field] < b[field])
      return ascending ? -1 : 1;

    if (a[field] > b[field])
      return ascending ? 1 : -1;

    return 0;

  });

};

/**
 * Debounce
 */
export const debounce = (
  callback: (...args: any[]) => void,
  delay = 500
) => {

  let timeout: ReturnType<typeof setTimeout>;

  return (...args: any[]) => {

    clearTimeout(timeout);

    timeout = setTimeout(() => {
      callback(...args);
    }, delay);

  };

};

/**
 * Extract API Error Message
 */
export const getErrorMessage = (
  error: any
): string => {

  return (
    error?.response?.data?.detail ||
    error?.response?.data?.message ||
    error?.message ||
    "Unexpected error occurred."
  );

};

/**
 * Download JSON File
 */
export const downloadJson = (
  filename: string,
  data: unknown
): void => {

  const blob = new Blob(
    [JSON.stringify(data, null, 2)],
    { type: "application/json" }
  );

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = filename;

  link.click();

  URL.revokeObjectURL(url);

};

/**
 * Convert Bytes to Human Readable Size
 */
export const formatFileSize = (
  bytes: number
): string => {

  if (bytes === 0)
    return "0 Bytes";

  const k = 1024;

  const sizes = [
    "Bytes",
    "KB",
    "MB",
    "GB",
    "TB",
  ];

  const i = Math.floor(
    Math.log(bytes) / Math.log(k)
  );

  return (
    parseFloat(
      (bytes / Math.pow(k, i)).toFixed(2)
    ) +
    " " +
    sizes[i]
  );

};

