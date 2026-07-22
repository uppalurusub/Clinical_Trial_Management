
interface LoaderProps {
  message?: string;
  size?: "sm" | "md" | "lg";
  variant?:
    | "primary"
    | "secondary"
    | "success"
    | "danger"
    | "warning"
    | "info"
    | "dark";
  fullScreen?: boolean;
}

const Loader = ({
  message = "Loading...",
  size = "md",
  variant = "primary",
  fullScreen = false,
}: LoaderProps) => {

  const spinnerSize =
    size === "sm"
      ? "spinner-border-sm"
      : size === "lg"
      ? "spinner-border"
      : "spinner-border";

  const containerClass = fullScreen
    ? "d-flex justify-content-center align-items-center vh-100"
    : "d-flex justify-content-center align-items-center p-5";

  return (
    <div className={containerClass}>

      <div className="text-center">

        <div
          className={`${spinnerSize} text-${variant}`}
          role="status"
          style={
            size === "lg"
              ? {
                  width: "4rem",
                  height: "4rem",
                }
              : {}
          }
        >
          <span className="visually-hidden">
            Loading...
          </span>
        </div>

        <div className="mt-3">

          <h6 className="text-muted">
            {message}
          </h6>

        </div>

      </div>

    </div>
  );

};

export default Loader;

