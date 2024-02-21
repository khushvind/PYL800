% Define the function as an inline function
a = input('Enter function: ', 's');
f = inline(a);

% Input for the interval [xl, xu]
xl = input('Enter the lower point of the guess interval: ');
xu = input('Enter the upper point of the guess interval: ');

% Input for the allowed error in calculation
e = input('Enter the allowed error in calculation: ');

% Input for the maximum number of iterations
max_iter = input('Enter the maximum number of iterations: ');

% Call the bisection method function
root = bisect(xl, xu, e, f, max_iter);

% Function definition for the bisection method
function root = bisect(xl, xu, e, f, max_iter)
    % Check for no sign change
    y=[];
    if f(xl) * f(xu) > 0
        disp('No sign change found in the given interval. There may be no root in this interval.');
        root = NaN;  % Return NaN if no root is found
        return;
    end
    a=xl;
    b=xu;
    xr = (xl + xu) / 2;  % First root estimate
    iter = 1;
    if f(xr)*f(xl) < 0
        xu = xr;
    else
        xl = xr;
    end
    
    while true
        y=[y xr];
        if abs(xl-xu) < e*(b-a) || iter >= max_iter
            break
        end
        xr = (xu + xl)/2;
        % Check the position of the new root
        if f(xr) * f(xu) < 0
            xl = xr;
        else
            xu = xr;
        end
        iter = iter + 1;
    end

    if iter >= max_iter
        disp('Maximum number of iterations reached. The root may not be accurate.');
    end

    root = xr;
    plot(y);
    disp('Root of this function by Bisection method is: ');
    disp(root);
    disp('Number of iterations used in Bisection method are: ');
    disp(iter);
end
